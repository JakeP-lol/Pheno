
from plantcv import plantcv as pcv 
import numpy as np
import os
import argparse
import matplotlib



def options():

    parser = argparse.ArgumentParser(description="PlantCV multi-plant workflow")
    parser.add_argument("--image", help="Input image", required=True)
    parser.add_argument("--result", help="Results file", required=True)
    parser.add_argument("--outdir", help="Output directory", required=True)
    parser.add_argument("--writeimg", help="Save output images", action="store_true")
    parser.add_argument("--debug", help="Set debug mode", default=None)
    args = parser.parse_args()
    return args

def main():

    args = options()

    pcv.params.debug = args.debug

    pcv.params.dpi = 100

    pcv.params.text_size = 10
    pcv.params.text_thickness = 20

    in_img, path, filename = pcv.readimage(filename=args.image)

    img = pcv.transform.rotate(img=in_img, rotation_deg=1, crop=True)

    colorspaces = pcv.visualize.colorspaces(rgb_img=img, original_img=False)

    a = pcv.rgb2gray_lab(rgb_img=img, channel='a')

    hist = pcv.visualize.histogram(img=a, bins=25)

    a_thresh = pcv.threshold.binary(gray_img=a, threshold=120, max_value=255, object_type='dark')

    a_fill = pcv.fill(bin_img=a_thresh, size=90)

    obj, obj_hierarchy = pcv.find_objects(img=img, mask=a_fill)

    rois, roi_hierarchy = pcv.roi.multi(img=img, coord=(1350,200), radius=175, 
                                        spacing=(450, 400), nrows=6, ncols=4)

    plant_ids = range(0, len(rois))

    img_copy = np.copy(img)

    pcv.params.debug = None

    for i in range(0, len(rois)):
 
        roi = rois[i]
        hierarchy = roi_hierarchy[i]
        plant_id = plant_ids[i]

        plant_contours, plant_hierarchy, mask, area = pcv.roi_objects(img=img, 
                                                                      roi_contour=roi, 
                                                                      roi_hierarchy=hierarchy, 
                                                                      object_contour=obj, 
                                                                      obj_hierarchy=obj_hierarchy, 
                                                                      roi_type="partial")


        if area > 0:

            plant_obj, plant_mask = pcv.object_composition(img=img, 
                                                           contours=plant_contours, 
                                                           hierarchy=plant_hierarchy)        

            img_copy = pcv.analyze_object(img=img_copy, obj=plant_obj, 
                                          mask=plant_mask, label=f"plant{plant_id}")
    pcv.plot_image(img_copy)
    pcv.outputs.save_results(filename=args.result, outformat="json")


    # In[ ]:




if __name__ == "__main__":
    main()
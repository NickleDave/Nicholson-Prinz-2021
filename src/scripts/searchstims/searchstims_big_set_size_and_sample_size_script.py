from pathlib import Path

import searchstims.make
from searchstims.stim_makers import RVvGVStimMaker, RVvRHGVStimMaker, Two_v_Five_StimMaker

ALEXNET_SIZE = (227, 227)
VGG16_SIZE = (224, 224)
BORDER_SIZE = (30, 30)
GRID_SIZE = (5, 5)
ITEM_BBOX_SIZE = (30, 30)
JITTER = 12

for window_size in (ALEXNET_SIZE,):
    keys = ['RVvGV', 'RVvRHGV', '2_v_5']
    vals = [
        RVvGVStimMaker(target_color='red',
                       distractor_color='green',
                       window_size=window_size,
                       border_size=BORDER_SIZE,
                       grid_size=GRID_SIZE,
                       item_bbox_size=ITEM_BBOX_SIZE,
                       jitter=JITTER),
        RVvRHGVStimMaker(target_color='red',
                         distractor_color='green',
                         window_size=window_size,
                         border_size=BORDER_SIZE,
                         grid_size=GRID_SIZE,
                         item_bbox_size=ITEM_BBOX_SIZE,
                         jitter=JITTER),
        Two_v_Five_StimMaker(target_color='white',
                             distractor_color='white',
                             window_size=window_size,
                             border_size=BORDER_SIZE,
                             grid_size=GRID_SIZE,
                             item_bbox_size=ITEM_BBOX_SIZE,
                             jitter=JITTER,
                             target_number=2,
                             distractor_number=5)
    ]
    if window_size == ALEXNET_SIZE:
        alexnet_zip = zip(keys, vals)
    elif window_size == VGG16_SIZE:
        vgg16_zip = zip(keys, vals)

OUTPUT_DIR = Path('../visual_search_stimuli/')
TARGET_PRESENT = [3600, 7200, 14400, 21600, 28800, 43200, 64800]
TARGET_ABSENT = [3600, 7200, 14400, 21600, 28800, 43200, 64800]
SET_SIZES = [1, 2, 4, 6, 8, 12, 18]


def main():
    for cnn, zipped in zip(['alexnet', ], [alexnet_zip, ]):
        for key, val in zipped:
            csv_filename = f'{cnn}_big_set_and_sample_size_{key}.csv'
            stim_dict = {key: val}
            output_dir = OUTPUT_DIR.joinpath(f'{cnn}_big_set_and_sample_size_{key}')
            searchstims.make.make(root_output_dir=output_dir,
                                  stim_dict=stim_dict,
                                  csv_filename=csv_filename,
                                  num_target_present=TARGET_PRESENT,
                                  num_target_absent=TARGET_ABSENT,
                                  set_sizes=SET_SIZES)


if __name__ == '__main__':
    main()

rm datasets/nsner/cached_crf-test_bert-base-chinese_512_nsner
python extra_str/prepare_test_data.py --path extra_str/test.txt
sh scripts/test.sh
python increment/get_entities.py
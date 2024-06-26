CURRENT_DIR=`pwd`
export BERT_BASE_DIR=$CURRENT_DIR/prev_trained_model/bert-base-chinese
export DATA_DIR=$CURRENT_DIR/datasets
export OUTPUT_DIR=$CURRENT_DIR/outputs
TASK_NAME="nsner"
#
python run_ner_crf.py \
  --model_type=bert \
  --model_name_or_path="$BERT_BASE_DIR" \
  --task_name=$TASK_NAME \
  --do_train \
  --do_eval \
  --do_lower_case \
  --data_dir="$DATA_DIR"/${TASK_NAME}/ \
  --train_max_seq_length=512 \
  --eval_max_seq_length=512 \
  --per_gpu_train_batch_size=8 \
  --per_gpu_eval_batch_size=8 \
  --learning_rate=3e-5 \
  --crf_learning_rate=1e-3 \
  --num_train_epochs=4\
  --logging_steps=-1 \
  --save_steps=-1 \
  --output_dir="$OUTPUT_DIR"/${TASK_NAME}_output/ \
  --overwrite_output_dir \
  --seed=42

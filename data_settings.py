from utils import get_data, data_hparams

# 0.准备训练所需数据------------------------------
train_data_args = data_hparams()
train_data_args.data_type = 'train'
train_data_args.data_path = 'E:/data/corpus/'
train_data_args.thchs30 = True
train_data_args.aishell = True
train_data_args.prime = True
train_data_args.stcmd = True
train_data_args.batch_size = 4
train_data_args.data_length = 500
# data_args.data_length = None
train_data_args.shuffle = False
train_data = get_data(train_data_args)

# 0.准备验证所需数据------------------------------
dev_data_args = data_hparams()
dev_data_args.data_type = 'dev'
dev_data_args.data_path = 'E:/data/corpus/'
dev_data_args.thchs30 = True
dev_data_args.aishell = True
dev_data_args.prime = False
dev_data_args.stcmd = False
dev_data_args.batch_size = 4
# data_args.data_length = None
dev_data_args.data_length = 100
dev_data_args.shuffle = True
dev_data = get_data(dev_data_args)
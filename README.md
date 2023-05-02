

# ALIGNN (source: https://github.com/usnistgov/alignn)

The Atomistic Line Graph Neural Network (https://www.nature.com/articles/s41524-021-00650-1)  introduces a new graph convolution layer that explicitly models both two and three body interactions in atomistic systems. 


conda create --name perl </br>
source activate perl


git clone https://github.com/SourinDeyUW/alignn.git </br>
cd alignn </br>
python setup.py develop --user </br>


pip install dgl-cu102 # import torch;print(torch.version.cuda) , if 10.2, then pip install dgl-cu102 </br>

unzip alignn_nmc_eig_HSE_individual_node_v3_april23_pbe.zip

python alignn/train_folder.py --root_dir "alignn/examples/sample_data"  --batch_size "16" --epochs 2 --config "alignn/examples/sample_data/config_example.json" --output_dir="demo_v1" >> output.txt






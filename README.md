

## ALIGNN (source: https://github.com/usnistgov/alignn)

The Atomistic Line Graph Neural Network (https://www.nature.com/articles/s41524-021-00650-1)  introduces a new graph convolution layer that explicitly models both two and three body interactions in atomistic systems. 

## Dataset generation (optional)
The csv file and cif files are large , I provided the generated dataloader in alignn_nmc_eig_HSE_individual_node_v3_april23_pbe.pickle in the zip file. The following 2 python files are used to generate this dataloader. Let me know if you want to run them. I will provide the link containing the dataset. 
First, run prepare_loader_part1.py </br>
Second, run prepare_loader_part2.py


## setting up 

conda create --name perl </br>
source activate perl


git clone https://github.com/SourinDeyUW/alignn_beast.git </br>
cd alignn_beast </br>
python setup.py develop --user </br>


pip install dgl-cu102 # import torch;print(torch.version.cuda) , if 10.2, then pip install dgl-cu102 </br>

unzip alignn_nmc_eig_HSE_individual_node_v3_april23_pbe.zip

python alignn/train_folder.py --root_dir "alignn/examples/sample_data"  --batch_size "16" --epochs 200 --config "alignn/examples/sample_data/config_example.json" --output_dir="demo_v1" >> output.txt






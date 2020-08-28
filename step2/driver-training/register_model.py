# Import libraries
import argparse
from azureml.core import Run

# Get parameters
parser = argparse.ArgumentParser()
parser.add_argument('--model_folder', type=str, dest='model_folder',
                    default="driver-training", help='model location')
args = parser.parse_args()
model_folder = args.model_folder

# Get the experiment run context
run = Run.get_context()

# load the model
print("Loading model from " + model_folder)
model_name = 'porto_seguro_safe_driver_model'
model_file = model_folder + "/" + model_name + ".pkl"

# Get metrics for registration
metrics = run.parent.get_metrics()
## HINT: Try storing the metrics in the parent run, which will be
##       accessible during both the training and registration
##       child runs using the 'run.parent' API.

# Register the model
run.upload_file(model_name, model_file)
run.register_model(
    model_path=model_name,
    model_name=model_name,
    tags=metrics)

run.complete()

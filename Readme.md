# Simple ML Pipeline with Argo Workflow

In this example we build a simple ML pipeline using argo worfklow.
our example uses the popular iris dataset. The pipeline consist of 3 steps

![iris-pipeline](https://user-images.githubusercontent.com/47831972/136802902-3133fa17-570e-4aaf-834d-00e9cdd157fd.PNG)

- <b>Generate Data (preprocessing)</b>: this is the step where our data is feteched and split into train and test sets. ideally we can also do other things in this step like cleaning the data if it's not in a format we want

- <b>Build Model (Model training and evaluation)</b>: in this step we use our preprocessed data from the previousstep to build a decision forest classifer. we then save the model as a pickl filed and save the test accuracy of the model. ideally we would want split this step into 2 or more steps so we can train our model in a sperate step and test the saved model in a different step

- <b>Output Result (Result reporting)</b>: in this step we simply display the test accuracy of our model. we can potentially make other types of reports if we want. in this example things have deliberatly been keept very simple.

# Pipeline

The yaml file used to generate the pipeline can be found in the pipeline folder
the src folder holds all of our code we converted to docker images used by our pipeline

to make our images easy to build an push, a base image is built with all the requirements every other step in our pipline can potentially need. if anything is ommited, we can easily run a pip install on top of our base image. so you would notice that everys step in our workflow uses the base image we built.

# What do I need to run the pipeline?

- install docker-desktop and start the kuberntes cluster that comes with docker desktop.

- install argo workflow following the instructions [here](https://argoproj.github.io/argo-workflows/quick-start/)

- you can either port-forward the argo server or expose a loadbalancer(you would find this info in the link above for installing argo workflow) and then visit https://localhost:2746 (note that you may not find argo on http and so protocol has to be https)

- you can then click on the submit new workflow button and click on edit using full workflow option ![argo-iris-submit](https://user-images.githubusercontent.com/47831972/136803556-14e816bb-12b5-42c1-8b8a-ed3352f7299c.PNG)

- you can then paste the content of the argo-iris.yaml into the UI and submit the workflow and wait for it to finish running.

# Got questions?

feel free to ask via the github issues or shoot me a message on [linkedin](https://www.linkedin.com/in/emmanuel-ogunwede-665404126/)

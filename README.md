[![Build Status](https://travis-ci.com/IBM/python-ubi-openshift.svg?branch=development)](https://travis-ci.com/IBM/python-ubi-openshift)

#  Deploy an application to OpenShift 4 using Redhat's universal base image

This code pattern is part of the [Bee Travels project](https://github.com/bee-travels) that focuses on deploying a python currency exchange application to OpenShift 4 using Redhat's universal base image.


## After following this code pattern, you will understand how to:

* Design and create a Python microservice with a REST interface that has a swagger test harness where you can manually inspect, discover, and run the various API endpoints.

* Build a docker image of this microservice using the RedHat Universal Base Image(UBI)
* Deploy and run this microservice on OpenShift version 4

## Architecture

This is the flow of the currency conversion microservice.

![architecture flow diagram](./doc/images/architecture.jpg)

***Figure 1: Architecture flow***

1. Client API Consumer calls the microservice over the internet (http/s request).
1. Flask process acts as a `web server` and accepts the REST request (e.g. GET /convertCurrency/ZAR/USD/600.66).
1. Code routing in Flask passes the request to a service module which in turn calls the External European Currency Exchange API (http://api.exchangeratesapi.io).
1. An exchange rate for ZAR is retrieved and stored. The value of 600.66 South African Rands (ZAR) is converted to US Dollars(USD).
1. Flask then sends a response to the calling consumer with the dollar amount (in this case, $40.59 ).


## Included components

* [IBM Cloud RedHat OpenShift version 4](https://www.ibm.com/cloud/openshift): Red Hat® OpenShift® on IBM Cloud™ is a fully managed OpenShift service that leverages the enterprise scale and security of the IBM Cloud.
* [Swagger](https://swagger.io/): A framework of API developer tools for the OpenAPI Specification that enables development across the entire API lifecycle.



## Featured technologies

* [Container Orchestration](https://www.ibm.com/cloud/container-service/): is the process of automating the deployment, scaling and management of containerized applications.

* [Microservices](https://www.ibm.com/cloud/architecture/architectures/microservices/): are an application architectural style in which an application is composed of many discrete, network-connected components called microservices.  They are collections of fine-grained, loosely coupled services intercommunicating via a lightweight protocol to provide building blocks in modern application composition in the cloud.

* [Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a micro [web framework](https://en.wikipedia.org/wiki/Flask_(web_framework)) written in Python. It is classified as a microframework because it does not require particular tools or libraries.

# Prerequisites
You need to have the following installed to complete the steps in this code pattern:

* [Docker](https://www.docker.com/products/docker-desktop)
* [IBM Cloud Account](https://cloud.ibm.com/registration)
* [IBM RedHat OpenShift 4 Cluster](https://cloud.ibm.com/kubernetes/catalog/openshiftcluster)
* OpenShift CLI tool [oc](https://cloud.ibm.com/docs/openshift?topic=openshift-openshift-cli#cli_oc)

# Steps 

Follow these steps to set up and run this code pattern locally and on the cloud. The steps are described in detail below.

1. [Clone the GitHub repository locally](#1-clone-the-GitHub-repository-locally)

2. [Build a docker image and run it locally](#2-build-and-run-a-docker-image-locally)

3. [Deploy to IBM RedHat OpenShift 4 Cluster](#3-deploy-to-openshift-4-cluster)

### 1. Clone the GitHub repository locally

Clone the `currencyexchange` GitHub repository locally.

In a terminal, run the following:

```bash
git clone https://github.com/IBM/python-ubi-openshift.git

cd python-ubi-openshift
```


### 2. Build and run a docker image locally

We showcase this method, by using the RedHat `Universal Base Image` (UBI)


## What is UBI?

### Introducing the RedHat Universal Base Image (UBI)

At the core of containers there is a lighter weight Linux operating system. Most of us may have used Ubuntu or Alpine as the base Operating system.

RedHat now offers us a good alternative base image, that is essentially the core
of RedHat Enterprise Linux.  Much like CentOS and RedHat Enteprise linux derive it's core elements from the OpenSource Fedora project.

This ***Linux alternative from RedHat*** is called the Universal Base Image (UBI)`.

The UBI comes in a few flavors:

1.  You can choose one of  three base images (`ubi`, `ubi-minimal` and `ubi-init`)
1.  Or Language specific runtime images (e.g. `node.js`, `python`, etc.)

UBI allows one to use associated packages via `YUM repositories` which satisfy common application dependencies, like `httpd` (apache web server) etc.



### Take a look at our [Dockerfile](./Dockerfile) and notice the `FROM` directive is using the UBI version 8 (core of RedHat 8) base image.

```yaml
FROM registry.access.redhat.com/ubi8/ubi
```

Now let's build this docker image with the `RedHat UBI`.


1. Make sure you are at the Root directory of this application.

1. Note your docker-hub username
<details><summary><strong>How to find your docker hub credentials</strong></summary>

> To download Docker desktop you must create a Docker hub account.

> To find the username, you can click on at your Docker desktop icon (mac) toolbar 

![Docker Desktop Find your logged-in username](./doc/images/docker-desktop-get-username.png)
</details>

1. Build the docker image by running:

```bash
export DOCKERHUB_USERNAME=<your-dockerhub-username>
docker build -t $DOCKERHUB_USERNAME/currencyexchange-py:v0.0.1 .
```

<details><summary><strong>Expected output details</strong></summary>

Here is a truncated snippet of the successful output you should see:

```bash
Sending build context to Docker daemon  69.63MB
Step 1/10 : FROM registry.access.redhat.com/ubi8/ubi
 ---> fd73e6738a95

 ...

Collecting flask (from -r requirements.txt (line 13))
  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)

 ...

Successfully built 3b5631170697
Successfully tagged <DOCKERHUB_USERNAME>/currencyexchange-py:v0.0.1
```

Notes:

* The docker build process, pulled the RedHat 8 Universal Base Image from the redhat registry.

* The base image is the generic image, i.e. ubi8/ubi.  We could have use the Python 3 language specic flavor of the image but opted for this version for 2 reasons:

1. to show off the yum install features

1. to show how a finer controlled version of the language could have been used, like in our case the latest version (at the time of writing) of Python version 3.8 (note to check docker file version to be sure!)


</details>

Great! So, now lets run the image locally!

```bash
docker run -p 7878:7878 $DOCKERHUB_USERNAME/currencyexchange-py:v0.0.1
```

At your command line run: `docker ps` and you should now confirm that the docker container for the currencyexchange microservice is up and running.

![UBI Docker](./doc/images/UBI-docker-ps.jpeg)

> Explore the microservice from your browser at
> [http://127.0.0.1:7878](http://127.0.0.1:7878) for documentation about this API's endpoints and a `try-it-out` test harness to actually run the API calls.

![expected browser swagger](./doc/images/expected-browser-swagger.png)


### 3. Deploy to OpenShift 4 cluster

1. To allow changes to the this microservice, create a repo on [Docker Cloud](https://cloud.docker.com/) where you can push the newly modified container. 


```bash
# build your docker image
export DOCKERHUB_USERNAME=<your-dockerhub-username>

docker build -t $DOCKERHUB_USERNAME/currencyexchange-py:v0.0.1 .

docker login

# push image to docker hub
docker push $DOCKERHUB_USERNAME/currencyexchange-py:v0.0.1

```
<details><summary><strong>What a successful push to docker hub should look like</strong></summary>

```bash
The push refers to repository [docker.io/claraxxxxxx/currencyexchange-py]
693f7ba0eeed: Pushed 
225cfc6f0260: Pushed 
2ddc888e45c8: Pushed 
1aac3cbf59e3: Pushed 
85f69e555a1b: Pushed 
1295eae54c9d: Pushed 
v0.0.1: digest: sha256:2aa41155a8bd44bb25tytytyt990ed4d5f455968ef88697463456f249a35654841d size: 1574
```
</details>


2. Provision an [IBM RedHat OpenShift 4 Service](https://cloud.ibm.com/kubernetes/catalog/openshiftcluster)
and follow the set of instructions for creating a Container and Cluster.

### There are 2 ways to deploy the image to OpenShift.

1. [Using the OC CLI](#Option-1-using-the-oc-cli)
2. [OpenShift web console](#Option-2-OpenShift-web-console)


#### Option 1. Using the OC CLI 
read more about the [OC CLI](https://cloud.ibm.com/docs/openshift?topic=openshift-openshift-cli#cli_oc)


Login to your OpenShift 4 cluster

![2 ways to connect to OpenShift cluster](doc/images/OpenShift-connection-to-cluster-2-ways.png)

click the Actions/Connect via CLI ( annotated with a number(1) above ) and follow the instructions:

use `oc login ... ` to login to your cluster, for example 
```sh
oc login --token=X8bjO-ROAhGUx8S9pvg6767574ysuG9SSgSI6hyg --server=https://c108-e.us-northwest.containers.cloud.ibm.com:31007
```

create a new project

```bash
oc new-project currencyexchange-py
```

you should be able to confirm this by typing:

```bash
oc project
```
and see

![confirm project is setup](doc/images/OpenShift-project-confirm-cli.png)




next add a new application

```bash
oc new-app $DOCKERHUB_USERNAME/currencyexchange-py:v0.0.1
```

Great!  Now you should see

![new application created with your image](doc/images/OpenShift-oc-new-application-created.png)

Note the yellow highlight section confirms that the RedHat UBI is the base image in your docker deployment.

Almost there!  You will need to expose the microservice to the outside world by executing

```bash
oc expose svc/currencyexchange-py

#expected output
> route.route.openshift.io/currencyexchange-py exposed

#get the external URL to access the microservice
oc status

```
![getting the external url](doc/images/OpenShift-get-external-url-cli.png)

So copy and paste the url indicated in yellow highlight above into your favorite web browser and voila!  You should see:

![OpenShift url shows swagger and exchange rate conversion executes as expected](doc/images/OpenShift-url-navigate-to-shows-swagger-success.png)


Looking at the OpenShift Web console we can now see our microservice all setup and running nicely.

![OpenShift Web console up and running](doc/images/OpenShift-webconsole-after-CLI-image-deploy.png)

#### Option 2. OpenShift web console

After provisioning your OpenShift cluster, click on the blue `OpenShift web console` button indicated by the number two(2) in the image below.

![2 ways to connect to OpenShift cluster](doc/images/OpenShift-connection-to-cluster-2-ways.png)


You should now see the web console.

Note that there are 2 ***perspectives*** of the web console, the `administrator` and the `developer`.  Switch to the developer view by clicking on the Administrator (default) option and selecting the Developer option indicate by the number two (2) in the image below 

![OpenShift web console switch to the developer perspective](doc/images/OpenShift-GUI-change-to-developer-perspective.png)

The ***Developer*** perspective in the web console provides you the following options from the Add view to create applications and associated services and deploy them on OpenShift Container Platform:

There are various options to choose from here, we will choose the `Container Image` where you will use the existing image you previously built and pushed to DockerHub and deploy it on your OpenShift Container Platform.

![OpenShift web console create app with container image](doc/images/OpenShift-GUI-dev-perspective-app-creation-choices-tile-highlighted-container-image.png)

<details><summary><strong>Learn more about application creation options as an OpenShift Developer</strong></summary>


1. From Git: Use this option to import an existing codebase in a Git repository to create, build, and deploy an application on OpenShift Container Platform.

1. Container Image: Use existing images from an image stream or registry to deploy it on to OpenShift Container Platform.

1. From Catalog: Explore the Developer Catalog to select the required applications, services, or source to image builders and add it to your project.

1. From Dockerfile: Import a dockerfile from your Git repository to build and deploy an application.

1. YAML: Use the editor to add YAML or JSON definitions to create and modify resources.

To learn more check out the [OpenShift developer documentation](https://docs.openshift.com/container-platform/4.3/applications/application_life_cycle_management/odc-creating-applications-using-developer-perspective.html#odc-creating-applications-using-developer-perspective)
</details>

Fill out the image name text box on your DockerHub repository.  It should be:

`$DOCKERHUB_USERNAME/currencyexchange-py:v0.0.1`

where `$DOCKERHUB_USERNAME` is you Docker hub username.

Click on the `search icon`  (magnifying glass) to the left of the text box.

It should fetch the image metadata from DockerHub and create a nice form.

![OpenShift Container image form](doc/images/OpenShift-container-image-after-search-details-of-image.png)

Click on the blue create button indicated with the number one(1) above.

Great!  You should now see a nice topology and summary of the application you just created:

![OpenShift](doc/images/OpenShift-GUI-container-image-created-successfully-maybe.png)

Click on the `currencyexchang...` button in the above screenshot, indicated by the number one(1) in the orange triangle.

You should now be able to click on the public URL  under the `Routes` section in the right hand panel. 

For example:

`http://currencyexchange-py-currencyexchange-py.username-ubi-webconso-f2c6cdc6801be85b09d0xxxxx06f13e3-0000.us-northeast.containers.appdomain.cloud/`

You should now see Python Flask swagger API interactive web page, where you can manually test the Currency Conversion as seen below. 

![OpenShift url shows swagger and exchange rate conversion executes as expected](doc/images/OpenShift-url-navigate-to-shows-swagger-success.png)



### Congratulations!  

You have now successfully created and deployed a microservice using the RedHat Universal Base Image (UBI) in an OpenShift 4 cluster on IBM Cloud












# Resources
[Introducing the Red Hat Universal Base Image ](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image) - RedHat blog by Scott McCarty



[Python RESTful APIs using flask-restplus](https://pypi.org/project/flask-restplus/)


## License

This code pattern is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)


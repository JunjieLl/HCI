## Assignment 3

## 1850668 李俊杰

[TOC]



## Environment

```shell
$ conda env create -f env.yaml
$ conda activate hci3
$ cd server && python rest-server.py
```

## Requirement of Image Search Task

The core function of the image search task is to retrieve the 9 most similar images in the database to the one uploaded by the user. At the same time, the system should provide corresponding user interfaces to allow the user to upload images, view search results, perform further operations on the results such as classification and collection, and some other functions such as downloading images.

## Design for 5 Stages

#### Data Structure Definition

The data returned by the server during image retrieval is defined as follows:

```json
{
    "images": [{
        "imageUrl": "/result/im599.jpg",
        "imageIndex": "599",
        "kinds": ["People_R1", "People", "Sunset", "Female", "Water"],
        "isFavo": false
    }, {
        "imageUrl": "/result/im1623.jpg",
        "imageIndex": "1623",
        "kinds": ["Flower_R1", "Plant_Life", "Flower"],
        "isFavo": true
    }],
    "kinds": ["Animals", "Bird", "Bird_R1", "Clouds", "Dog", "Dog_R1", "Female", "Flower", "Flower_R1", "Indoor", "Lake", "Male", "Male_R1", "People", "People_R1", "Plant_Life", "Portrait", "Portrait_R1", "Sea", "Sky", "Structures", "Sunset", "Water"]
}
```

Each object in 'images' fields includes the image's URL, index in the database, categories and whether it is favorited. At the same time, the 'kinds' field contains the categories of images involved in the search result.

The data submitted to the server when collecting images is defined as follows:

```json
{
  "imageIndex": "522",
  "isFavo": true
}
```

It contains the index of the image in the database and whether it is favorited.

#### Formulation & Initiation

The user first selects the image to be uploaded, which will be displayed below the search box (only appear when the image is selected). After that, the user uploads the image to the server, which executes the image retrieval task and returns the result, and the web renders the result for the user.

Before selecting an image:

![image-20220508165557752](https://tva1.sinaimg.cn/large/e6c9d24egy1h213m8898jj21k50u0dgn.jpg)

After selecting an image:

![image-20220508165444940](https://tva1.sinaimg.cn/large/e6c9d24egy1h213kyebppj21k20u0wgf.jpg)

When uploading an image:

![image-20220508165650719](https://tva1.sinaimg.cn/large/e6c9d24egy1h213n4byjsj21k50u0mz6.jpg)

#### Review

Users can view retrieved images and their categories, and can view the number of retrieved images.

![image-20220508165834232](https://tva1.sinaimg.cn/large/e6c9d24egy1h213ox8s6uj21kg0u0jv1.jpg)

![image-20220508165853851](https://tva1.sinaimg.cn/large/e6c9d24egy1h213p9pucbj21ko0u0wj9.jpg)



#### Refinement

Above the search results, there are also classification options, and users can classify the results by clicking on the options.

![image-20220508170926879](https://tva1.sinaimg.cn/large/e6c9d24egy1h214088s1wj21jm04yjsj.jpg)

After selecting some classification options, the web will display the classified results (here, the number of images that satisfy the classification is 5).

![image-20220508171006220](https://tva1.sinaimg.cn/large/e6c9d24egy1h2140wsh2lj21k20u078s.jpg)

#### Use

Users can also bookmark images and download images, by clicking the corresponding star icon and image.

![image-20220508171615083](https://tva1.sinaimg.cn/large/e6c9d24egy1h214la0tcoj21jb0u0wix.jpg)


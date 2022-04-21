<div style="text-align: center;font-size:25px;">济事楼4楼导览手机APP设计</div>
<div style="text-align: center;">1850668 李俊杰</div>

#### 1.手势设计介绍

由于是手机APP[^2]，屏幕较小，所以主要的交互方式是手势，根据Shortcuts should be used consistently across applications，手势的设计与现有APP、操作系统是一致的，几乎不需要学习，本APP中涵盖的手势有：

* Tap: 用于选择
* Double Tap：用于收藏
* Small Swipe：用于轻扫以上滑底部栏，平移地图，向左轻扫以删除数据项
* Pinch and Spread：用于双指捏合以缩放和旋转

#### 2.主页

![主页](https://tva1.sinaimg.cn/large/e6c9d24ely1h1hn7dh4ltj20by0ny3zi.jpg)

根据`Graphical techniques are an attractive way to present choices`，所以利用SketchUp工具设计了济事楼4楼3D图[^1]，且由于屏幕较小，本着`less is more`的原则，将App主要功能以3D的方式展现出来，让用户一看就知道怎么去操作：利用手势：

1. 双指捏合缩放地图
2. 双指中一指固定另一指移动旋转地图
3. 单指平移地图

这些手势是跨应用的，都是用户熟悉的，没有学习成本（`Learnability is key`）。

同时APP还提供了AR视角，让用户可以体验增强现实的便利性。

另外还有底部栏，放在后面介绍。

#### 2.手势操作

![手势旋转缩放](https://tva1.sinaimg.cn/large/e6c9d24ely1h1hn7if5uej20by0ny75b.jpg)

用户在对地图进行操作（包括1中提到的旋转、平移、缩放和点击具体房间）时，底部栏会自动收缩从而增大用户的操作空间，只留出搜索框便于用户进行快速搜索和选择，3D图使得用户可以从空间上各个角度观看楼层平面布局。

#### 3.点击具体的房间

![点击具体的房间](https://tva1.sinaimg.cn/large/e6c9d24ely1h1hn7mrvisj20by0nyt9p.jpg)

用户可以在地图上通过点击房间查看信息，在点击具体的房间后，在该房间上方会有Pop Up显示该房间的具体信息，为了与其它APP如电话交互，用户可以直接点击某些字段如电话进而通过确认拨打该房间的电话。同时根据`Consider use frequency and importance`，用户可以通过点击收藏图标对房间进行收藏或是通过快捷手势双击房间进行收藏，以便在下次进入APP时可以快速定位（见底部栏介绍）到收藏的房间。

#### 4.AR视角

![ar](https://tva1.sinaimg.cn/large/e6c9d24ely1h1hn7p0rarj20by0ny0u9.jpg)

APP提供了AR视角以提供更加沉浸的交互体验，交互方式与3D视角的相同。

#### 5.底部栏

![底部栏上拉](https://tva1.sinaimg.cn/large/e6c9d24ely1h1hn7rc5bpj20by0nyt98.jpg)

底部栏用户只需在主页轻轻向上扫就可以占满屏幕，根据`Consider use frequency and importance`，展示了用户收藏的房间以及最近访问的房间，用户通过点击对应的房间图标就可以在地图上快速定位到指定房间，同时根据`Strive to reduce or eliminate data entry`，在主页面上没有显示过多关于房间的信息，房间的具体信息可以通过点击更多按钮进行查看，房间的具体信息与搜索页面中一致，在此不再展示。

###### 6.搜索

![搜索](https://tva1.sinaimg.cn/large/e6c9d24ely1h1hn7vwrcjj20by0nywf5.jpg)

当用户点击搜索框时，底部栏会自动铺满屏幕，便于键盘放置和展示搜索结果。在搜索框中支持关键字查询，即只要通过与该房间有关的信息都可以检索到该房间，如搜索`葛蕾`，这里的数据项同时也是5的更多中展示的数据项，只是在5中用户可以通过向左轻扫来扫出删除按钮，进而进行删除收藏和历史记录。搜索完成后，用户点击取消按钮或是下拉（只需要在任意位置向下轻扫）即可取消。



[^1]:可能会在作业截止后将模型上传到SketchUp网站，暂时没有在附件中给出。
[^2]:设计采用Axure完成。
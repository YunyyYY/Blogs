---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---

## Ruby

### Gems

A gem is code you can include in Ruby projects. It allows you to package up functionality and share it across other projects or with other people. Gems can perform functionality such as:

-   Converting a Ruby object to JSON
-   Pagination
-   Interacting with APIs such as GitHub
-   Jekyll itself is a gem as well as many Jekyll plugins

**gem命令：**用于构建、上传、下载以及安装Gem包。

**gemfile：**包含当前Ruby项目需要运行的Gems列表。

当我们需要为Jekyll项目添加插件时，我们可以使用Gemfiles来指定。需要在Gemfiles文件的开头，至少指定一个gem source(指向RubyGems server的url)；可以通过执行命令`bundle init`来创建一个gemfile，其默认source为`https://rubygems.org`。在Gemfile中的`gem "jekyll-seo-tag"`相当于单独执行命令`gem install 'jekyll-seo-tag'`；但前者只应用与当前项目，后者则属于全局安装与某个项目无关。

当我们更改了Gemfile文件后，需要运行`bundle install`命令，该命令生成Gemfile.lock文件，并下载该文件中的gems。

```sh
bundle install --path vendor/bundle
```

一般我们在初次运行 `bundle install`时会使用`--path`选项，该选项用于指定该项目中使用到的 Gems 的下载安装路径；之后使用`bundle install`时就无需指定`--path`。

<br>

### Bundler

**Bundler：**一个用于管理应用依赖关系的通用工具，它可以跟 RubyGems 搭配使用。通过Bundler程序读取Gemfile然后下载文件中需要的Gems。用于在Ruby库中管理Rubygems依赖项。

`bundle exec`只会使用Gemfile中该gem需要的版本。执行`bundle exec jekyll serve`或`jekyll serve`后便会生成一个`_site`目录，这就是生成的网站。使用版本控制时建议排除`_site`目录。Before `building` the site, it actually doesn't exist and is just a bunch of template files。

<br>



## jeklyy

`jekyll new`命令：该命令会使用默认的主题，创建一个新的jekyll网站框架(项目)

`jekyll serve`作用：

1.  构建站点（使用build命令）
2.  启动开发服务器，并在默认情况下监测文件变化并进行实时构建。任何时候发生变化将自动构建网站。

`jekyll build`：该命令用于创建静态站点(生成`_site`目录)。

生成文件的路径可以在`config.yml`中配置，路径格式类似`_site/2017-01-19/style-test-ko/index.html`。其中`_site根目录 = url + baseurl`，`title`目录为style-stest-ko，它是这篇文章的标题，最终的文章内容将保存在`index.html`文件中。

<br>

### structure

```
.
├── _config.yml
├── _drafts
|   ├── begin-with-the-crazy-ideas.textile
|   └── on-simplicity-in-technology.markdown
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   └── post.html
├── _posts
|   ├── 2007-10-29-why-every-programmer-should-play-nethack.textile
|   └── 2009-04-26-barcamp-boston-4-roundup.textile
├── _site
├── .jekyll-metadata
└── index.html
```

<br>

### `_config.yml`

保存配置数据。很多配置选项都可以直接在命令行中进行设置，但是如果你把那些配置写在这儿，你就不用非要去记住那些命令了。

部署GitHub pages的URL配置：

```
 # URL
 url:                "https://fandean.github.io" # the base hostname & protocol for your site
 # url:                "http://localhost:4000" # use this url when you develop
 baseurl:            "\blog" # the subpath of your site, e.g. /blog
 # homepage URL for the website： url + baseurl = https://fandean.github.io/blog
```

 To create links on the pages:

```yaml
links:
  - name:         Posts
    url:          /
    external:     false
  - name:         About me
    url:          /about
    external:     false
```



For technical reasons, this file is *NOT* reloaded automatically when you use `bundle exec jekyll serve`. If you change this file, please restart the server process using `bundle update`.

<br>

### `index.html`

在站点的根目录。这个文件将是Jekyll生成站点的主页。

在主页上的布局：站点上任何 HTML 文件，包括主页，都可以使用 layout 和 include 中的内容作为公用的内容，如页面的 header 和 footer. 将合适的部分抽出放到布局中。

<br>

### Front matter

Anything with [YAML](https://yaml.org/) header info will be treated as a special file in Jekyll. The front matter must be the first thing in the file and must take the form of valid YAML set between triple-dashed lines.

```yaml
---
layout: post
title: Blogging Like a Hacker
---
```

在这两行的三虚线之间，你可以设置预定义的变量甚至创建一个你自己定义的变量。这样在接下来的文件和任意模板中或者在包含这些页面或博客的模板中都可以通过使用 Liquid 标签来访问这些变量。

>   **WARNING**
>
>   如果使用 UTF-8 编码，那么文件中一定不要出现 `BOM` 头字符

可以在页面或者博客的头信息里设置已经**预定义好的全局变量**:

-   `layout`: 如果设置的话，会指定使用该模板文件。指定模板文件时候不需要文件扩展名。模板文件必须放在 `_layouts` 目录下。
-   `permalink`: 如果你需要让你发布的博客的 URL 地址不同于默认值(可在`_config.yml`中定义)，那你就设置这个变量，然后变量值就会作为最终的 URL 地址。
-   `published`: 如果你不想在站点生成后展示某篇特定的博文，那么就设置（该博文的）该变量为 false。

也可以设置[自定义的全局变量](https://jekyllcn.com/docs/frontmatter/)。

<br>

### `_post`

posts的命名必须遵循特定的格式：
```markdown
yyyy-mm-dd-name_of_post.md
```
否则在编译的时候jekyll会找不到post。同时post的开头也要遵循特定格式：

Sample post:

```markdown
---
layout: post
title:  "Welcome to Jekyll!"
date:   2019-09-21 10:23:46 -0400
categories: jekyll update
---

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}
```

<br>

### Categories

https://blog.webjeda.com/jekyll-categories/

## Gem-based themes

To replace layouts or includes in your theme, make a copy in your `` or `` directory of the specific file you wish to modify, or create the file from scratch giving it the same name as the file you wish to override.

For example, if your selected theme has a `page` layout, you can override the theme’s layout by creating your own `page` layout in the `_layouts` directory (that is, `_layouts/page.html`).

<br>

### Reference

1.  https://jekyllrb.com/docs/
2.  https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll
3.  [jekyll install and deploy](https://faner.gitlab.io/blog/2017/07/07/jekyll安装与部署/#heading-jekyll本地安装)
4.  [jekyll github](https://github.com/jekyll/jekyll)
5.  YAML syntax:
    -   https://learn-the-web.algonquindesign.ca/topics/markdown-yaml-cheat-sheet/#yaml
    -   https://learnxinyminutes.com/docs/yaml/
6.  [writing blogs](https://jekyllcn.com/docs/posts/)
7.  [Sample website](https://github.com/link9596/hydrogen)

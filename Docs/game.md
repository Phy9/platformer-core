---
title: "game"
author: "topazand"
date: "1/24/2020"
output:
  html_document: 
    keep_md: yes
    toc: true
    toc_float: true
---


```r
library(reticulate)
use_python("/usr/bin/python")
```

## level

```python
game.Level
```

_game object for represnting levels_


```python
game.Level(levelname, caming = None)
```

**Description**

returns a game level object

**Arguments**

levelname: {levelname}.json file in levels folder

caming: 

***


```python
game.Level.init_camera(camargs)
```
**Description**

Initialize camera position


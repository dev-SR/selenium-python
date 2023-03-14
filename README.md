# Selenium Python

- [Selenium Python](#selenium-python)
  - [Installation](#installation)
  - [Selectors Basics](#selectors-basics)


## Installation

```bash
pipenv install selenium pandas webdriver-manager
```

## Selectors Basics

```html
//tagName[@attributeName='attributeValue']
//tagName[contains(@attributeName,'substring')]
//tagName[@attr1="attValue1"][@attr2="attValue2"]
//tagName[@attr1="attValue1" and @attr2="attValue2"]
//tagName[@attr1="attValue1" or @attr2="attValue2"]
//tagName[text()="textValue"]
//tagName[contains(text(),"substring")]
//tagName[normalize-space()="textValue")]
//tagName[.="textValue")]
//tagName[last()]
//tagName[position=number]
(xpath)[index]

```

```html
<div>
 <a href="">Images</a>
</div>

//a[.='Images']
//a[contains(text(),"mag")]

<a href="">Images</a>

//div[.='Images']

<div>
 <a href="">Images</a>
</div>
```

<!--  -->

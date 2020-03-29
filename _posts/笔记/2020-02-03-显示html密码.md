---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---

The usual setting for HTML password is:

<div>
    <label for="pass">Password (8 characters minimum):</label>
    <input type="password" id="pass" name="password" minlength="8" required="">
</div>

```html
<div>
    <label for="pass">Password (8 characters minimum):</label>
    <input type="password" id="pass" name="password" minlength="8" required="">
</div>
```

To view the password, open inspector, and find the `<div>` for this password. Change the type of input from "password" to "text" and the password content will show:

<div>
    <label for="pass">Password (8 characters minimum):</label>
    <input type="text" id="pass" name="password" minlength="8" required="">
</div>

```html
<div>
    <label for="pass">Password (8 characters minimum):</label>
    <input type="password" id="pass" name="password" minlength="8" required="">
</div>
```


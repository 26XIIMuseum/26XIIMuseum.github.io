
## Comments / Discussion

- disable

## Styles

- appearance -> editor -> styles -> browse style -> evening color scheme and platypi & ysabeau office typography
- review & save
- styles -> typography -> ELEMENTS -> text -> letter spacing 1.0px
- styles -> typography -> font size presets -> M, L, and XL -> min 2 rem max 2 rem
- review & save

## Fonts

- allow wordpress to download fonts directly from Google
- install the Hanken Grotesk font

## Additional CSS

- browse to `http://<foobar>/wp-admin/customize.php` > Additional CSS

```
h1.wp-block-site-title > a {
	text-decoration: none;
	color: white;
	transition: color 0.2s ease-in-out !important;
}

h1.wp-block-site-title > a:hover {
	text-decoration: none !important;
	color: #1c95d1 !important;
}


h1 > a {
  font-family: "Sabon" !important;
}

a.mega-menu-link {
	margin-bottom: 1rem !important;
	color: white;
	transition: color 0.2s ease-in-out !important;
}

a.mega-menu-link:hover {
	color: #1c95d1 !important;
}

.fa {
  font-family: FontAwesome !important;
}
```

## Header

- appearance -> editor -> select header right hand rendered page.  Alternatively, while on the homepage, Edit Site
- in the right panel, select design -> Header inside full-width background
- select document overview to get tree list of header elements


## Menu

- install Max Mega Menu
- create a new menu for Header location
- edit the header, delete the Nav, add the Max Mega Menu
- ensure the menu is "enabled" in Menu Locations
- set colors
- change font size to 1.8 rem for Menu Bar and Mobile Menu


## Lightbox

- install Firelight Lightbox by FirelightWP


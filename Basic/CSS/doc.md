# CSS tips and trick

## position absolute relative to parent
> [stack overflow](https://stackoverflow.com/questions/10487292/position-absolute-but-relative-to-parent)

> This works because position: absolute means something like "use top, right, bottom, left to position yourself in relation to the nearest ancestor who has position: absolute or position: relative."
>
> So we make #father have position: relative, and the children have position: absolute, then use top and bottom to position the children.
```css
#father {
		position: relative;
}

#son {
		position: absolute;
		top: 0;
}
```

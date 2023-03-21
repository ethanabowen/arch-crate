# Process AWS Architecture Icons

- Rename Files for easier understanding
- Transform SVGs
  - Make Background transparent
  - Move Icon up and scale down
  - Add text of Service Name below Icon
    - Call text-to-svg local server. See [https://github.com/ethanabowen/text-to-svg](https://github.com/ethanabowen/text-to-svg). Remove SVG block from response.
    - Modify for transformations (translate and scale)
    -
  - Fill svg with Black or White using boolean flag _IS_BLACK_FILL_

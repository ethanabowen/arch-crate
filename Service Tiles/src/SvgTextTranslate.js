const svg = document.children[0]
const svgRect = svg.getBoundingClientRect();
const svgWidth = svgRect.width

const svgText = document.getElementById('svgGroup');
const svgTextRect = svgText.getBoundingClientRect();
const svgTextWidth = Math.round((svgTextRect.width + Number.EPSILON) * 100) / 100;

//var tfm = svgTextRect.createSVGTransform();
//tfm.setTranslate(width, '80%');
//svgText.transform.baseVal.appendItem(tfm)
const finalTextAdjustedWidth = svgRect.width / 2 - svgTextWidth / 2;
const finalTextAdjustedHeight = svgRect.height * .8;

svgText.setAttribute("transform", "translate(" + finalTextAdjustedWidth + ", " + finalTextAdjustedHeight + ")")

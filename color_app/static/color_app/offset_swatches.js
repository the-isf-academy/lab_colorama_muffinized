// Offset Swatches
// This is a litle JavasScript function which adds a 50% margin to the first 
// swatch in every even row, creating a pleasant offset. This function is called
// when the page loads, and then whenever the page is resized. 

let oddRow = false;
let x = undefined

function getWidth(className) {
	return document.getElementsByClassName(className)[0].getBoundingClientRect().width
}
function offsetSwatches() {
  const swatchWidth = getWidth("swatch")
	const swatchesWidth = getWidth("swatches")
	const swatchesPerOddRow = Math.floor(swatchesWidth / swatchWidth)
	const swatchesPerEvenRow = Math.floor((swatchesWidth - (swatchWidth/2)) / swatchWidth)

	const palettes = document.getElementsByClassName("swatches")
	for (let p=0; p < palettes.length; p++) {
	  const swatches = palettes[p].getElementsByClassName("swatch")
	  for (let i=0; i < swatches.length; i++) {
	    const swatch = swatches[i]
		  if (i % (swatchesPerOddRow + swatchesPerEvenRow) === swatchesPerOddRow) {
				  swatch.style['margin-left'] = '' + (swatchWidth / 2) + 'px'
		  }
		  else {
				  swatch.style['margin-left'] = '0'
	    }
    }
	}
}

window.addEventListener('resize', offsetSwatches)
offsetSwatches()

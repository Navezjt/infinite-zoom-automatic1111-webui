// mouseover tooltips for various UI elements

infzoom_titles = {
    "Batch Count":"How many separate videos to create",
    "Total video length [s]":"For each seconds frame (FPS) will be generated. Define prompts at which time they should start wihtin this duration.",
    "Common Prompt Prefix":"Prompt inserted before each step",
    "Common Prompt Suffix":"Prompt inserted after each step",
    "Negative Prompt":"What your model shall avoid",
    "Export prompts": "Downloads a JSON file to save all prompts",
    "Import prompts": "Restore Prompts table from a specific JSON file",
    "Clear prompts": "Start over, remove all entries from prompt table, prefix, suffix, negative",
    "Custom initial image":"An image at the end resp. begin of your movie, depending or ZoomIn or Out",
    "Custom exit image":"An image at the end resp. begin of your movie, depending or ZoomIn or Out",
    "Zoom Speed":"Varies additional frames per second",
    "Start at second [0,1,...]": "At which time the prompt has to be occure. We need at least one prompt starting at time 0",
	"Generate video": "Start rendering. If it´s disabled the prompt table is invalid, check we have a start prompt at time 0"
}


onUiUpdate(function(){
	gradioApp().querySelectorAll('span, button, select, p').forEach(function(span){
		tooltip = infzoom_titles[span.textContent];

		if(!tooltip){
		    tooltip = infzoom_titles[span.value];
		}

		if(!tooltip){
			for (const c of span.classList) {
				if (c in infzoom_titles) {
					tooltip = infzoom_titles[c];
					break;
				}
			}
		}

		if(tooltip){
			span.title = tooltip;
		}
	})

	gradioApp().querySelectorAll('select').forEach(function(select){
	    if (select.onchange != null) return;

	    select.onchange = function(){
            select.title = infzoom_titles[select.value] || "";
	    }
	})
})

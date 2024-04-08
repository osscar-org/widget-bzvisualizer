import { createBZVisualizer } from "brillouinzone-visualizer";

function render({ model, el }) {
  let getSeekpathData = () => model.get("seekpath_data");

  let getShowAxes = () => model.get("show_axes");
  let getShowBVectors = () => model.get("show_bvectors");
  let getShowPathpoints = () => model.get("show_pathpoints");
  let getDisableInteractOverlay = () => model.get("disable_interact_overlay");

  let container = document.createElement("div");
  container.style.width = model.get("width");
  container.style.height = model.get("height");
  container.style.margin = "0 auto";

  let mainBZVisualizer = createBZVisualizer(container, getSeekpathData(), {
    showAxes: getShowAxes(),
    showBVectors: getShowBVectors(),
    showPathpoints: getShowPathpoints(),
    disableInteractOverlay: getDisableInteractOverlay(),
  });

  model.on("change:seekpath_data", () => {
    mainBZVisualizer.loadBZ(getSeekpathData());
  });

  el.appendChild(container);
}

export default { render };

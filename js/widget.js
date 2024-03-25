import { createBZVisualizer } from "brillouinzone-visualizer";

function render({ model, el }) {
  let getSeekpathData = () => model.get("seekpath_data");

  let container = document.createElement("div");
  container.style.width = model.get("width");
  container.style.height = model.get("height");
  container.style.margin = "0 auto";

  el.appendChild(container);

  let mainBZVisualizer = createBZVisualizer(container, getSeekpathData());

  model.on("change:seekpath_data", () => {
    mainBZVisualizer.loadBZ(getSeekpathData());
  });
}

export default { render };

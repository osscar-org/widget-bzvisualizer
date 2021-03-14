var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'widget-bzvisualizer:plugin',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'widget-bzvisualizer',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};


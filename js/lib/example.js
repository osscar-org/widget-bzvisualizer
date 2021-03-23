var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');
var $ = require('jquery');
var BZVisualizer = require('./BZVisualizer').BZVisualizer;

require('../css/brillouin.css');

// See example.py for the kernel counterpart to this file.


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var BrillouinZoneModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name: 'BrillouinZoneModel',
        _view_name: 'BrillouinZoneView',
        _model_module: 'widget-bzvisualizer',
        _view_module: 'widget-bzvisualizer',
        _model_module_version: '0.1.0',
        _view_module_version: '0.1.0',
        value: 'BrillouinZone World!'
    })
});


// Custom View. Renders the widget model.
var BrillouinZoneView = widgets.DOMWidgetView.extend({

    initialize: function () {
        this.canvasID = _.uniqueId("BZCanvas");
        this.infoID = _.uniqueId("info");
        this.BZVisualizer = new BZVisualizer(true, true, true, false);
    },

    // Defines how the widget gets rendered into the DOM
    render: function () {
        // Observe changes in the value traitlet in Python, and define
        // a custom callback.
        this.model.on('change:kpts', this.kpts_changed, this);
        this.model.on('change:face_color', this.faceColor_changed, this);

        this.el.innerHTML = '<div class="BZ-widget" id="' + this.canvasID + '"></div>'
            + '<div id="' + this.infoID + '"></div>';

        var jsondata = this.model.get('jsondata');
        var faceColor = this.model.get('face_color');

        that = this;
        $(document).ready(function () {
            that.BZVisualizer.loadBZ(canvasID=that.canvasID, infoID=that.infoID, jsondata=jsondata);
            that.BZVisualizer.set_visibility(faceColor);
        });
    },

    kpts_changed: function () {
        const kpts = this.model.get('kpts');
        this.BZVisualizer.update_kpts(kpts);
    },

    faceColor_changed: function() {
        this.BZVisualizer.set_visibility(this.model.get('face_color'));
    }
});


module.exports = {
    BrillouinZoneModel: BrillouinZoneModel,
    BrillouinZoneView: BrillouinZoneView
};

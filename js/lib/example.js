var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');
var $ = require('jquery');
var BZVisualizer = require('brillouinzone-visualizer').BZVisualizer;
// var BZVisualizer = require('./BZVisualizer').BZVisualizer;

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

    events: {
        'keypress #BZ-widget': 'toggle_faceColor',
    },

    // Defines how the widget gets rendered into the DOM
    render: function () {
        // Observe changes in the value traitlet in Python, and define
        // a custom callback.
        this.model.on('change:kpts', this.kpts_changed, this);
        this.model.on('change:face_color', this.faceColor_changed, this);
        this.model.on('change:path_vectors', this.vectors_changed, this);
        this.model.on('change:update_structure', this.reloadBZ, this);

        this.height = this.model.get('height');
        this.width = this.model.get('width');

        this.el.innerHTML = '<div class="BZ-widget" id="' + this.canvasID
            + '" style="height:' + this.height + '; width:' + this.width + ';"'
            + '></div><div id="' + this.infoID + '"></div>';

        var jsondata = this.model.get('jsondata');
        var faceColor = this.model.get('face_color');

        that = this;
        $(document).ready(function () {
            that.BZVisualizer.loadBZ(canvasID = that.canvasID, infoID = that.infoID, jsondata = jsondata);
            that.BZVisualizer.set_visibility(faceColor);
        });
    },

    reloadBZ: function () {
        var jsondata = this.model.get('jsondata');
        var faceColor = this.model.get('face_color');

        this.BZVisualizer.loadBZ(canvasID = this.canvasID, infoID = this.infoID, jsondata = jsondata);
        this.BZVisualizer.set_visibility(faceColor);
    },

    toggle_faceColor: function (event) {
        console.log("The key press is working.********:" + event.keyCode);

        if (event.keyCode == 84) {
            const faceColor = this.model.get('face_color');
            this.model.set('face_color', !faceColor);
            this.touch();
        }
    },

    kpts_changed: function () {
        const kpts = this.model.get('kpts');
        this.BZVisualizer.update_kpts(kpts);
    },

    vectors_changed: function () {
        const vectors = this.model.get('path_vectors');
        this.BZVisualizer.update_pathVector(vectors);
    },

    faceColor_changed: function () {
        this.BZVisualizer.set_visibility(this.model.get('face_color'));
    }
});


module.exports = {
    BrillouinZoneModel: BrillouinZoneModel,
    BrillouinZoneView: BrillouinZoneView
};

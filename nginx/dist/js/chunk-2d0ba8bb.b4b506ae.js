(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0ba8bb"],{3855:function(t,e,a){"use strict";a.r(e);var o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-flex",[t.resource.tags&&t.resource.tags.length>0?a("v-flex",[a("v-flex",t._l(t.resource.tags,(function(e){return a("v-btn",{key:e.name,staticClass:"font-weight-bold text-lowercase",attrs:{color:e.color,small:"",round:""}},[t._v(" "+t._s(e.name)+" "),a("v-icon",{attrs:{right:""},on:{click:function(a){return a.stopPropagation(),t.tag_to_resource(e)}}},[t._v("mdi-close-circle")])],1)})),1)],1):a("v-flex",[t._v("No tags")]),t.show_tags?a("v-flex",[t.tags.length>0?a("v-flex",[a("v-label",[t._v("Available tags")]),a("v-flex",t._l(t.available_tags,(function(e){return a("v-btn",{key:e.name,staticClass:"font-weight-bold text-lowercase",attrs:{color:e.color,small:"",round:""},on:{click:function(a){return t.tag_to_resource(e)}}},[t._v(t._s(e.name))])})),1)],1):a("v-flex",[t._v("No tags yet")]),a("v-flex",[a("v-dialog",{attrs:{width:"250"},scopedSlots:t._u([{key:"activator",fn:function(e){var o=e.on;return[a("v-btn",t._g({attrs:{flat:"",icon:""}},o),[a("v-icon",{attrs:{color:"green"}},[t._v("mdi-plus")])],1)]}}],null,!1,3356724318),model:{value:t.tag_dialog,callback:function(e){t.tag_dialog=e},expression:"tag_dialog"}},[a("v-card",[a("v-card-title",[t._v("Name")]),a("v-card-text",[a("v-text-field",{ref:"tag_name_field",attrs:{outline:"","single-line":"",required:"",label:"no spaces, only alpha"},model:{value:t.new_tag_name,callback:function(e){t.new_tag_name="string"===typeof e?e.trim():e},expression:"new_tag_name"}})],1),a("v-divider"),a("v-card-title",[t._v("Color")]),a("v-layout",{attrs:{row:"","pb-3":""}},[a("v-flex",{attrs:{xs12:""}},t._l(t.tag_colors,(function(e){return a("v-btn",{key:e,attrs:{value:e,fab:"",dark:"",small:"",color:e},on:{click:function(a){a.stopPropagation(),t.new_tag_color=e}}})})),1)],1),a("v-divider"),a("v-card-actions",[a("v-flex",[a("v-btn",{attrs:{color:"primary"},on:{click:function(e){return e.stopPropagation(),t.new_tag()}}},[t._v("add")])],1)],1)],1)],1)],1)],1):t._e()],1)},n=[],r=(a("4de4"),a("45fc"),a("b0c0"),a("7c15")),l={name:"Tags",props:{resource:{type:Object,default:{}},show_tags:{type:Boolean,default:!1}},data:function(){return{tags:[],tag_dialog:!1,tag_colors:[],new_tag_name:null,new_tag_color:"blue"}},computed:{available_tags:function(){var t=this;return void 0===this.resource.tags?this.tags:this.tags.filter((function(e){return!t.resource.tags.some((function(t){return t.name===e.name}))}))}},methods:{new_tag:function(){this.tag_dialog=!this.tag_dialog;var t={name:this.new_tag_name,color:this.new_tag_color},e={url:"/api/add_new_tag",tag:t};Object(r["a"])(e),this.new_tag_color="blue",this.$refs.tag_name_field.reset(),this.load_tags()},load_tags:function(){var t=this,e={url:"/api/get_tags"};Object(r["a"])(e).then((function(e){return t.tags=e.data.tags})),e={url:"/api/get_tag_colors"},Object(r["a"])(e).then((function(e){return t.tag_colors=e.data.tag_colors}))},tag_to_resource:function(t){var e=this,a={url:"/api/tag_to_resource",resource_id:this.resource._id,resource_type:this.resource.resource_type,tag:t};Object(r["a"])(a).then((function(t){e.$emit("shake")}))}},mounted:function(){this.load_tags()}},s=l,c=a("2877"),i=Object(c["a"])(s,o,n,!1,null,null,null);e["default"]=i.exports}}]);
//# sourceMappingURL=chunk-2d0ba8bb.b4b506ae.js.map
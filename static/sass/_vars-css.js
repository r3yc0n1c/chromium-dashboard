import {css} from 'lit';

export const VARS = css`
:root {
  --default-font-color: #222;
  --page-background: #fafafa;
  
  --light-grey: #eee;
  
  --gray-1: #e6e6e6;
  --gray-2: #a9a9a9;
  --gray-3: #797979;
  --gray-4: #515151;
  
  --nav-link-color: #444;
  
  --bar-shadow-color: rgba(0, 0, 0, .065);
  --bar-border-color: #D4D4D4;
  
  --chromium-color-dark: #366597;
  --chromium-color-medium: #85b4df;
  --chromium-color-light: #bdd6ed;
  --chromium-color-center: #4580c0;
  
  --material-primary-button: #58f;
  
  --card-background: white;
  --card-border: 1px solid #ddd;
  --card-box-shadow: rgba(0, 0, 0, 0.067) 1px 1px 4px;
  
  --md-yellow-100: #FFF9C4;
  --md-yellow-200: #FFF59D;
  
  /* App specific */
  --invalid-color: rgba(255,0,0,0.75);
  --content-padding: 16px;
  --default-border-radius: 3px;
  
  --app-drawer-width: 200px;
  --header-height: 135px;
  --max-content-width: 760px;
}`;
/* ----- */

// @mixin width-max-content() {
//   width: -webkit-max-content,
//   width: -moz-max-content,
//   width: -ms-max-content,
//   width: -o-max-content,
//   width: max-content,
// }

// @mixin width-min-content() {
//   width: -webkit-min-content,
//   width: -moz-min-content,
//   width: -ms-min-content,
//   width: -o-min-content,
//   width: min-content,
// }

// @mixin calc(property, expression) {
//   #{property}: -moz-calc(#{expression}),
//   #{property}: -o-calc(#{expression}),
//   #{property}: -webkit-calc(#{expression}),
//   #{property}: calc(#{expression}),
// }

// @mixin calc-width(val) {
//   width: -webkit-calc(val),
//   width: -moz-calc(val),
//   width: -ms-calc(val),
//   width: -o-calc(val),
//   width: calc(val),
// }

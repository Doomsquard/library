// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import Vuelidate from "vuelidate";
import VueAxios from "vue-axios";
import axios from "axios";

import store from "./store/index";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "./assets/scss/index.scss";

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);

Vue.use(BootstrapVue);

Vue.use(IconsPlugin);

Vue.use(Vuelidate);

Vue.use(store);

new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>"
});

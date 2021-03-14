import Vue from "vue";
import Router from "vue-router";
import signPage from "../pages/signPage";

Vue.use(Router);

const routes = [
  {
    path: "/signin",
    name: "signInPage",
    component: signPage
  },
  {
    path: "/signup",
    name: "signUpPage",
    component: signPage
  }
];

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

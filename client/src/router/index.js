import Vue from "vue";
import Router from "vue-router";
import signPage from "../pages/signPage";
import libraryPage from "../pages/libraryPage";
import Header from "../components/header";
import booksPage from "../pages/booksPage";
import downloadPage from "../pages/downloadPage";
import profilePage from "../pages/proflePage";

Vue.use(Router);

const headerComponent = name => {
  return { path: "", name: name, component: resolve => resolve(Header) };
};

const routes = [
  {
    path: "/library",
    component: libraryPage,
    children: [headerComponent("libraryPage")]
  },
  {
    path: "/profile",
    component: profilePage,
    children: [headerComponent("profilePage")]
  },
  {
    path: "/books",
    component: booksPage,
    children: [headerComponent("booksPage")]
  },
  {
    path: "/download",
    component: downloadPage,
    children: [headerComponent("downloadPage")]
  },
  {
    path: "/signin",
    name: "signInPage",
    component: signPage
  },
  {
    path: "/signup",
    name: "signUpPage",
    component: signPage
  },
  {
    path: "/*",
    name: "notFindPath",
    redirect: {
      path: "/library"
    }
  }
];

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

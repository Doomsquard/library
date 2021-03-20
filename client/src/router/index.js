import Vue from "vue";
import Router from "vue-router";
import signPage from "../pages/signPage";
import libraryPage from "../pages/libraryPage";
import Header from "../components/header";
import booksPage from "../pages/booksPage";
import downloadPage from "../pages/downloadPage";
import profilePage from "../pages/proflePage";
import store from "../store/index";

Vue.use(Router);

const headerComponent = name => {
  return { path: "", name: name, component: resolve => resolve(Header) };
};

const routes = [
  {
    path: "/library",
    meta: { auth: true },
    component: libraryPage,
    children: [headerComponent("libraryPage")]
  },
  {
    path: "/profile",
    meta: { auth: true },
    component: profilePage,
    children: [headerComponent("profilePage")]
  },
  {
    path: "/books",
    meta: { auth: true },
    component: booksPage,
    children: [headerComponent("booksPage")]
  },
  {
    path: "/download",
    meta: { auth: true },
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

const rout = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

rout.beforeEach((to, from, next) => {
  const currentUser = store.getters["userModule/getToken"];
  const requireAuth = to.matched.some(record => record.meta.auth);
  if (requireAuth && !currentUser && rout.history.current.path !== "/signin") {
    next("/signin");
  } else {
    next();
  }
  next();
});
export default rout;

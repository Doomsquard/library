import axios from "axios";
import store from "../store/index";
import { getCookieByName } from "../cookies/methods";

const instance = axios.create({
  baseURL: "http://127.0.0.1:5000/api/",
  headers: { "Access-Control-Allow-Origin": "*" }
});

instance.interceptors.request.use(request => {
  let currentToken = null;
  if (request.url === "/token/refresh" || request.url === "/logout/refresh") {
    currentToken =
      store.getters["tokenModule/getRefreshToken"] ||
      getCookieByName("jwtRefresh");
  } else {
    currentToken = store.getters["tokenModule/getToken"];
  }
  store.dispatch["tokenModule/checkToken"];

  request.headers["Authorization"] = `Bearer ${currentToken}`;

  return request;
});

export default instance;

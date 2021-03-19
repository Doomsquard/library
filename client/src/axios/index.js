import axios from "axios";
import store from "../store/index";
import jwt_decode from "jwt-decode";
import { getCookieByName } from "../cookies/methods";

const instance = axios.create({
  baseURL: "http://127.0.0.1:5000/api/",
  headers: { "Access-Control-Allow-Origin": "*" }
});

instance.interceptors.request.use(request => {
  console.log(request);
  if (request.url === "/token/refresh") {
    const currentToken = getCookieByName("jwtRefresh");
    store.dispatch["userModule/checkToken"];
    request.headers["Authorization"] = `Bearer ${currentToken}`;
    return request;
  } else {
    const currentToken = store.getters["userModule/getToken"];
    request.headers["Authorization"] = `Bearer ${currentToken}`;
    return request;
  }
});

export default instance;

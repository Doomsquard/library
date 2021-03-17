import axios from "axios";

export default axios.create({
  baseURL: "http://127.0.0.1:5000/api/",
  headers: { "Access-Control-Allow-Origin": "*" }
});

// export const setAuthToken = token => {
//     if (token) {
//     //applying token
//     instance.defaults.headers.common['Authorization'] = token;
//     } else {
//     //deleting the token from header
//      delete instance.defaults.headers.common['Authorization'];
//     }
// }

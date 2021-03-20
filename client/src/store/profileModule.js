import Api from "../axios/index";
import store from "./index";

export default {
  namespaced: true,
  state: {
    login: "",
    favbooks: null,
    favgenre: null,
    readed: null,
    wantread: null,
    birhday: null
  },
  getters: {
    getInfo(state) {
      return {
        login: state.login,
        favbooks: state.favbooks,
        favgenre: state.favgenre,
        readed: state.readed,
        wantread: state.wantread,
        birthday: state.birhday
      };
    },
    checkUser(state) {
      return state.login;
    }
  },
  mutations: {
    SET_PROFILE_DATA(state, payload) {
      state.login = payload.login;
      (state.favbooks = payload.favbooks.slice(1)),
        (state.favgenre = payload.favgenre.slice(1));
      (state.readed = payload.readed),
        (state.wantread = payload.want_read),
        (state.birhday = payload.birthday);
    }
  },
  actions: {
    getProfileData({ commit }, payload) {
      commit("SET_PROFILE_DATA", payload);
    }
  }
};

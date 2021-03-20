import Vue from "vue";
import Vuex from "vuex";
import userModule from "./userModule";
import profileModule from "./profileModule";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: { userModule, profileModule },
  state: {
    errorMsg: ""
  },
  getters: {
    getError(state) {
      return state.errorMsg;
    }
  },
  mutations: {
    SET_ERROR(state, payload) {
      state.errorMsg = payload;
    },
    NULL_ERROR(state) {
      state.errorMsg = "";
    }
  },
  actions: {
    setError({ commit }, payload) {
      commit("SET_ERROR", payload);
    },
    nullError({ commit }) {
      commit("NULL_ERROR");
    }
  }
});

export default {
  namespace: true,
  state: {
    currentUser: null
  },
  getters: {
    getPath(state) {
      return state.currentUser;
    }
  },
  mutations: {
    SET_USER(state, payload) {
      state.currentUser = payload;
    }
  },
  actions: {
    loadPath({ commit }, payload) {
      commit("SET_USER", payload);
    }
  }
};

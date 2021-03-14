<template>
  <main class="form-signin">
    <form class="form">
      <div class="d-flex">
        <img
          class="logo"
          src="../assets/images/brainbook.svg"
          width="50px"
          alt="logo"
        />
        <h1 class="h3 mb-3 fw-normal">BrainLibrary</h1>
      </div>

      <input
        v-show="!signIn"
        type="text"
        id="inputLogin"
        class="form-control"
        placeholder="Login"
        required=""
        v-model.trim="form.login"
      />

      <input
        type="text"
        id="inputEmail"
        class="form-control"
        placeholder="Email address"
        required=""
        kl_ab.original_type="email"
        v-model.trim="form.email"
      />

      <input
        type="password"
        id="inputPassword"
        class="form-control"
        placeholder="Password"
        required=""
        v-model.trim="form.password"
      />

      <input
        v-show="!signIn"
        type="date"
        id="inputDate"
        class="form-control"
        placeholder="Date of Birth"
        required=""
        kl_ab.original_type="date"
        v-model.trim="form.date"
      />

      <div class="checkbox mb-3" v-show="signIn">
        <label>
          <input type="checkbox" v-model="form.remember" /> Remember me
        </label>
      </div>

      <button class="w-100 btn btn-lg btn-primary m-2" type="submit">
        {{ signTitle }}
      </button>
      <div class="buttonRegister">
        <p class="fw-normal" @click="toSignUp">
          {{ regText }}
        </p>
      </div>
      <p class="mt-5 mb-3 text-muted">© 2021</p>
    </form>
  </main>
</template>

<script>
export default {
  name: "signComponent",
  data() {
    return {
      signIn: true,
      form: {
        email: "",
        password: "",
        login: "",
        date: "",
        remember: false
      }
    };
  },
  created() {
    this.$router.history.current.name === "signInPage"
      ? (this.signIn = true)
      : (this.signIn = false);
  },
  methods: {
    toSignUp() {
      if (this.signIn) {
        this.signIn = false;
        this.$router.push({ path: "signup" });
      } else {
        this.signIn = true;
        this.$router.push({ path: "signin" });
      }
      this.form.email = "";
      this.form.password = "";
      this.form.login = "";
      this.form.date = "";
      this.form.remember = false;
    }
  },
  computed: {
    signTitle() {
      return this.signIn ? "Sign in" : "Sign up";
    },
    regText() {
      return this.signIn ? "not registered yet?" : "already registered?";
    }
  }
};
</script>

<style lang="scss" scoped>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
  .form {
    margin-top: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    .form-control {
      margin-top: 10px;
    }

    .logo {
      margin: 0 5px 15px 0px;
    }
  }
  .buttonRegister {
    opacity: 0.7;
    cursor: pointer;
    transition: 0.2s;
    &:hover {
      opacity: 1;
    }
  }
}
</style>

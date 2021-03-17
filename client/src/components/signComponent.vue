<template>
  <main class="form-signin" ref="main" @click="e => resFormErrors(e)">
    <form
      class="form"
      @submit.prevent="submitHandler"
      novalidate
      name="signForm"
    >
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
        v-if="!loading"
        type="text"
        id="inputLogin"
        class="form-control"
        :class="loginError.class"
        placeholder="Login"
        required=""
        v-model.trim="form.login"
      />
      <b-skeleton
        v-show="!signIn"
        v-else
        type="input"
        class="form-control"
      ></b-skeleton>

      <b-form-text
        class="errorMessage"
        v-show="loginError.errorMessage ? true : false"
        id="password-help-block"
      >
        {{ loginError.errorMessage }}
      </b-form-text>

      <input
        v-if="!loading"
        type="text"
        id="inputEmail"
        class="form-control"
        placeholder="Email"
        required=""
        :class="emailError.class"
        kl_ab.original_type="email"
        v-model.trim="form.email"
      />

      <b-skeleton v-else type="input" class="form-control"></b-skeleton>

      <b-form-text
        class="errorMessage"
        v-show="emailError.errorMessage ? true : false"
        id="password-help-block"
      >
        {{ emailError.errorMessage }}
      </b-form-text>

      <input
        v-if="!loading"
        type="password"
        id="inputPassword"
        class="form-control"
        placeholder="Password"
        required=""
        v-model.trim="form.password"
        :class="passwordError.class"
      />

      <b-skeleton v-else type="input" class="form-control"></b-skeleton>

      <b-form-text
        class="errorMessage"
        v-show="passwordError.errorMessage ? true : false"
        id="password-help-block"
      >
        {{ passwordError.errorMessage }}
      </b-form-text>

      <input
        v-if="!loading"
        v-show="!signIn"
        type="password"
        id="samePassword"
        class="form-control"
        placeholder="Repeat password"
        required=""
        :class="passwordSameError.class"
        v-model.trim="form.samePassword"
      />
      <b-skeleton
        v-show="!signIn"
        v-else
        type="input"
        class="form-control"
      ></b-skeleton>

      <b-form-text
        class="errorMessage"
        v-show="passwordSameError.errorMessage ? true : false"
        id="password-help-block"
      >
        {{ passwordSameError.errorMessage }}
      </b-form-text>

      <input
        v-if="!loading"
        v-show="!signIn"
        type="date"
        id="inputDate"
        class="form-control"
        placeholder="Date of Birth"
        required=""
        :class="dateError.class"
        kl_ab.original_type="date"
        v-model.trim="form.date"
      />
      <b-skeleton
        v-else
        v-show="!signIn"
        type="input"
        class="form-control"
      ></b-skeleton>

      <b-form-text
        class="errorMessage"
        v-show="dateError.errorMessage ? true : false"
        id="password-help-block"
      >
        {{ dateError.errorMessage }}
      </b-form-text>

      <div class="checkbox mb-3" v-if="!loading" v-show="signIn">
        <label>
          <input type="checkbox" v-model="form.remember" /> Remember me
        </label>
      </div>

      <b-skeleton
        v-else
        v-show="!signIn"
        type="input"
        class="form-control"
      ></b-skeleton>

      <button
        :disabled="isloading"
        class="w-100 btn btn-lg btn-primary m-2"
        type="submit"
      >
        {{ signTitle }}
      </button>

      <div class="buttonRegister">
        <p class="fw-normal" @click="toSignUp">
          {{ regText }}
        </p>
      </div>
      <b-alert v-show="form.error" fade show="5s" variant="danger"
        ><a href="#" class="alert-link">{{ form.error }}</a></b-alert
      >
      <p class="mt-5 mb-3 text-muted">© 2021</p>
    </form>
  </main>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength, email, sameAs } from "vuelidate/lib/validators";

import Api from "../axios";

export default {
  mixins: [validationMixin],
  name: "signComponent",
  data() {
    return {
      signIn: true,
      loading: false,
      form: {
        email: "",
        password: "",
        samePassword: "",
        login: "",
        date: "",
        error: "",
        remember: false
      }
    };
  },
  validations: {
    form: {
      email: { email, required },
      password: {
        required,
        minLength: minLength(8),
        goodPassword: password => {
          return (
            password.length >= 8 &&
            /[a-z]/.test(password) &&
            /[A-Z]/.test(password) &&
            /[0-9]/.test(password)
          );
        }
      },
      date: { required },
      login: { required, minLength: minLength(4) },
      samePassword: {
        sameAsPassword: sameAs("password"),
        minLength: minLength(8),
        required
      }
    }
  },
  created() {
    this.$router.history.current.name === "signInPage"
      ? (this.signIn = true)
      : (this.signIn = false);
  },
  methods: {
    resFormErrors(e) {
      const parent = this.$refs.main.parentNode;
      e.stopPropagation();
      parent.addEventListener("click", () => {
        this.$v.form.$reset();
      });
    },

    toSignUp() {
      if (this.signIn) {
        this.signIn = false;
        this.$router.push({ path: "signup" });
      } else {
        this.signIn = true;
        this.$router.push({ path: "signin" });
      }
      this.$v.form.$reset();
      this.form.email = "";
      this.form.password = "";
      this.form.samePassword = "";
      this.form.login = "";
      this.form.date = "";
      this.form.remember = false;
    },
    submitHandler() {
      if (!this.signIn) {
        this.$v.form.$touch();
        if (!this.$v.form.$error) {
          this.loading = true;

          Api.post("/auth/signup", {
            login: this.form.login,
            email: this.form.email,
            password: this.form.password,
            birthday: this.form.date
          })

            .then(data => {
              console.log(data.data);
              this.loading = false;
              this.$router.push({ path: "/library" });
            })
            .catch(err => {
              this.resetErrorMessage(err.response.data.message);
              this.loading = false;
            });
        }
      } else {
        this.$v.form.email.$touch();
        this.$v.form.password.$touch();
        if (!this.$v.form.email.$error && !this.form.password.$error) {
          this.loading = true;

          Api.post("/auth/signin", {
            email: this.form.email,
            password: this.form.password
          })

            .then(data => {
              console.log(data.data);
              this.loading = false;
              this.$router.push({ path: "/library" });
            })
            .catch(err => {
              this.resetErrorMessage(err.response.data.message);
              this.loading = false;
            });
        }
      }
    },
    resetErrorMessage(errorMsg) {
      this.form.error = errorMsg;
      setTimeout(() => {
        return (this.form.error = "");
      }, 5000);
    }
  },
  computed: {
    isloading() {
      return this.loading ? true : false;
    },
    loginError() {
      if (this.$v.form.login.$error) {
        return {
          class: "error",
          errorMessage: "This is a required field with at least 4 characters"
        };
      } else {
        return {
          class: ""
        };
      }
    },
    emailError() {
      if (this.$v.form.email.$error) {
        return {
          class: "error",
          errorMessage: "Incorrect email"
        };
      } else {
        return {
          class: ""
        };
      }
    },
    passwordError() {
      if (this.$v.form.password.$error) {
        return {
          class: "error",
          errorMessage:
            "Must be at least 8 characters and contain a lowercase character, uppercase character and a number."
        };
      } else {
        return {
          class: ""
        };
      }
    },
    passwordSameError() {
      if (this.$v.form.samePassword.$error) {
        return {
          class: "error",
          errorMessage: "Password mismatch"
        };
      } else {
        return {
          class: ""
        };
      }
    },
    dateError() {
      if (this.$v.form.date.$error) {
        return {
          class: "error",
          errorMessage: "Enter your date of birth"
        };
      } else {
        return {
          class: ""
        };
      }
    },
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
  .error {
    border-color: red;
  }
}
</style>

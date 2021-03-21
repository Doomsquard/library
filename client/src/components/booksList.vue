<template>
  <div class="overflow-auto container booksList">
    <h3>{{ title }}</h3>
    <b-table
      v-if="list.length"
      id="my-table"
      :items="totalList"
      :per-page="perPage"
      :current-page="currentPage"
      small
    ></b-table>
    <h4 v-else>Your list is empty</h4>

    <b-pagination
      v-show="list.length"
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
    <b-form @submit.prevent="submitHandler">
      <b-form-group
        class="form-group"
        maxlength="50"
        :id="'input-group-' + currentId"
        :label="'New ' + place + ':'"
        :label-for="'input-' + currentId"
      >
        <b-form-input
          maxlength="50"
          :id="'input-' + currentId"
          v-model="form.name"
          :placeholder="'Enter new ' + place"
          required
        ></b-form-input>
      </b-form-group>
      <b-button variant="outline-primary" class="buttton-submit" type="submit"
        >add {{ place }}</b-button
      >
    </b-form>
  </div>
</template>

<script>
import { generateId } from "../resourses/id";
export default {
  name: "booksList",
  props: {
    list: Array,
    title: String,
    currentId: String,
    place: String
  },
  data() {
    return {
      perPage: 3,
      currentPage: 1,
      form: {
        name: ""
      }
    };
  },
  computed: {
    rows() {
      return this.list.length ? this.list.length : 1;
    },
    totalList() {
      return this.list.map((item, index) => {
        return { Number: index + 1, book: item };
      });
    }
  },
  methods: {
    submitHandler() {
      this.$store.dispatch(`profileModule/addFav${this.place}`, {
        id: generateId,
        name: this.form.name
      });
      this.form.name = "";
    }
  }
};
</script>

<style lang="scss" scoped>
.buttton-submit {
  margin-top: 10px;
  border-color: rgb(194, 194, 194);
  color: rgb(71, 71, 71);
  &:hover {
    background-color: rgb(194, 194, 194);
  }
  &:active {
    border-color: rgb(194, 194, 194) !important;
    background-color: rgb(194, 194, 194) !important;
    color: rgb(71, 71, 71) !important;
  }
  &:focus {
    border-color: rgb(194, 194, 194) !important;
    background-color: rgb(194, 194, 194) !important;
    color: rgb(71, 71, 71) !important;
    box-shadow: none !important;
    outline: none !important;
    -webkit-box-shadow: none !important;
  }
}
.booksList {
  margin: 50px;
  max-width: 400px;
}
.form-group {
  margin: auto;
}
@media screen and (max-width: 600px) {
  .booksList {
    margin: 0px;
  }
}
</style>

<!-- Sidebar.vue -->
<template>
  <div>
    <div class="sidebar" :class="{ open: isOpen }">
      <button class="close-btn" @click="toggleSidebar">Close</button>
      <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
      </ul>
    </div>
    <button class="open-btn" @click="toggleSidebar">Open Sidebar</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false
    };
  },
  methods: {
    toggleSidebar() {
      this.isOpen = !this.isOpen;
    }
  }
};
</script>

<style scoped>
.sidebar {
  width: 250px;
  height: 100%;
  position: fixed;
  top: 0;
  left: -250px;
  background-color: #111;
  color: white;
  transition: 0.3s;
  padding-top: 60px;
}

.sidebar.open {
  left: 0;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
}

.sidebar ul li {
  padding: 10px;
  text-align: center;
}

.sidebar ul li a {
  color: white;
  text-decoration: none;
}

.close-btn,
.open-btn {
  background-color: #111;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  position: fixed;
}

.close-btn {
  top: 10px;
  right: 20px;
}

.open-btn {
  top: 10px;
  left: 20px;
}
</style>

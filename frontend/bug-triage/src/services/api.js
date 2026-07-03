import axios from "axios";

const api = axios.create({
  baseURL: "https://issue-pilot-bug-triage.onrender.com",
});

export default api;

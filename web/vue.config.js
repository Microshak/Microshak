const { defineConfig } = require('@vue/cli-service')
const path = require('path');
module.exports = {
  //outputDir: '../main/resources/',
  //assetsDir: '../assets/sound/',
  // ...
  devServer: {
    open: process.platform === 'darwin',
    host: '0.0.0.0',
    port: 8081, // CHANGE YOUR PORT HERE!
   
  },
  // ...
}
var path = require('path')
var utils = require('./utils')
var config = require('../config')
var vueLoaderConfig = require('./vue-loader.conf')
var HtmlWebpackPlugin = require('html-webpack-plugin')
function resolve(dir) {
  return path.join(__dirname, '..', dir)
}

module.exports = {
  entry: {
    admin_cd: './src/admin_cd.js', //社团部管理 club department
    index: './src/index.js',
    admin_club: './src/admin_club.js' //社长管理
  },
  output: {
    path: config.build.assetsRoot,
    filename: '[name].js',
    publicPath: process.env.NODE_ENV === 'production'
      ? config.build.assetsPublicPath
      : config.dev.assetsPublicPath
  },
  plugins: [
    new HtmlWebpackPlugin(
      {
        title: '建平中学学生社团系统',
        filename: 'index.html',
        chunks: [
          'vendor',
          'manifest',
          'index',
        ],
        template:'index.html'
      }
    ),
    new HtmlWebpackPlugin(
      {
        title: '建平中学学生社团系统--社团部管理',
        filename: 'admin_cd.html',
        chunks: [
          'vendor',
          'manifest',
          'admin_cd',
        ],
        template: 'app_cd.html',
      }
    ),
    new HtmlWebpackPlugin(
      {
        title: '建平中学学生社团系统--社长管理',
        filename: 'admin_club.html',
        chunks: [
          'manifest',
          'vendor',
          'admin_club'
        ],
        template: 'app_club.html',
      }
    )

  ],
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      '@': resolve('src')
    }
  },
  module: {
    rules: [
      {
        test: /\.(js|vue)$/,
        loader: 'eslint-loader',
        enforce: 'pre',
        include: [resolve('src'), resolve('test')],
        options: {
          formatter: require('eslint-friendly-formatter')
        }
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: vueLoaderConfig
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        include: [resolve('src'), resolve('test')]
      },
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 50000,
          name: utils.assetsPath('img/[name].[hash:7].[ext]')
        }
      },
      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('fonts/[name].[hash:7].[ext]')
        }
      }
    ]
  }
}

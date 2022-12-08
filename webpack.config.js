const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode: 'development',
  devServer: {
    devMiddleware: {
      writeToDisk: true,
    },
  },
  context: __dirname,
  entry: { exercises: './static/js/exercises/index.ts' },
  module: {
    rules: [
      {
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  output: {
    path: path.resolve('./static/webpack_bundles/'),
    filename: '[name]-[hash].js',
  },
  plugins: [new BundleTracker({ filename: './webpack-stats.json' })],
};

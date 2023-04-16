import React, { Component } from 'react'
// 导入所需组件
import Clock from '../components/Clock'
import Loadpng from '../components/Loadpng'
// 导入路由依赖
import { Route,BrowserRouter, Routes } from 'react-router-dom'
 
export default class index extends Component {
  render() {
    return (
        // 使用BrowserRouter包裹，配置路由
      <BrowserRouter>
         {/* 配置路由默认页，exact严格匹配 */}
         <Routes>
        <Route element={<Clock />} path='/' exact></Route>
        <Route element={<Clock />} path='/clock'></Route>
        <Route element={<Loadpng />} path='/png'></Route>
        </Routes>
      </BrowserRouter>
    )
  }
}

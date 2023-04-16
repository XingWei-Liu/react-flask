// import Switch from './components/Switch.js';
import { useState } from 'react';
import React from 'react';

import { FileOutlined, PieChartOutlined, UserOutlined, DesktopOutlined, TeamOutlined } from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, theme } from 'antd';

import Clock from './components/Clock.js';
import ButtonEvent from './components/ButtonEvent.js';
import Loadpng from './components/Loadpng.js';

const { Header, Content, Footer, Sider } = Layout;

function getItem(label, key, icon, children) {
  return {
    key,
    icon,
    children,
    label,
  };
}
const items = [
  getItem('Option 1', '1', <PieChartOutlined />),
  getItem('Option 2', '2', <DesktopOutlined />),
  getItem('User', 'sub1', <UserOutlined />, [
    getItem('Tom', '3'),
    getItem('Bill', '4'),
    getItem('Alex', '5'),
  ]),
  getItem('Team', 'sub2', <TeamOutlined />, [getItem('Team 1', '6'), getItem('Team 2', '8')]),
  getItem('Files', '9', <FileOutlined />),
];




       
export default function App () {
  const [collapsed, setCollapsed] = useState(false);

  const [component, setComponent] = React.useState(true);
  
  // let component = "";

  const {
    token: { colorBgContainer },
  } = theme.useToken();


  const menuClick = (item) => {
    console.log("menu %s select", item.key);
    switch(item.key){
      case '1':
        setComponent("Clock");
        break;
      case '2':
        setComponent("ButtonEvent");
        break;
      case '3':
        setComponent("Loadpng");
        break;
      default:
        setComponent("Clock");
    }
  }

  const do_switch = () => {
    console.log("menu %s in switch", component);
    switch (component) {
    case 'Clock':
        return <Clock />
    case 'ButtonEvent':
        return <ButtonEvent />
    case 'Loadpng':
        return <Loadpng />
    default:
        return <Clock />
    }
  };

  return(
    <Layout
  style={{
    minHeight: '100vh',
  }}
>
  <Sider collapsible collapsed={collapsed} onCollapse={(value) => setCollapsed(value)}>
    <div
      style={{
        height: 32,
        margin: 16,
        background: 'rgba(255, 255, 255, 0.2)',
      }}
    />
    <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={items} onClick={menuClick}/>
  </Sider>
  <Layout className="site-layout">
    <Header
      style={{
        padding: 0,
        background: colorBgContainer,
      }}
    />
    <Content
      style={{
        margin: '0 16px',
      }}
    >
      <Breadcrumb
        style={{
          margin: '16px 0',
        }}
      >
        <Breadcrumb.Item>User</Breadcrumb.Item>
        <Breadcrumb.Item>Bill</Breadcrumb.Item>
      </Breadcrumb>
      <div
        style={{
          padding: 24,
          minHeight: 360,
          background: colorBgContainer,
        }}
      >
        {do_switch()}
      </div>
    </Content>
    <Footer
      style={{
        textAlign: 'center',
      }}
    >
      Ant Design ©2023 Created by Ant UED
    </Footer>
  </Layout>
</Layout>
  )
};
// export default App;

// // import logo from './logo.svg';
// import './App.css';
// import Router from './route/index'

//       <Router></Router>

// //<Clock name='datetime'/>
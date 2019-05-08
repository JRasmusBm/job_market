import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"
import OrderOverview from "../components/orderoverview"

const IndexPage = () => (
  <Layout>
    <SEO title="Job Market Explorer" keywords={[`job`, `market`, `offers`]} />
    <OrderOverview />
  </Layout>
)

export default IndexPage

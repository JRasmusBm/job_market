import * as React from "react"
import * as PropTypes from "prop-types"
import { Link, useStaticQuery, graphql } from "gatsby"

const OrderOverview = () => {
  const {server} = useStaticQuery(
    graphql`
      query {
        server {
          hello(argument: "Rasmus")
        }
      }
    `
  )
  return <main>{server.hello}</main>
}

export default OrderOverview

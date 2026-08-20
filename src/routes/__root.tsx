import { createRootRoute, Outlet, ScrollRestoration } from "@tanstack/react-router";
import "../styles.css";

export const Route = createRootRoute({
  component: Root,
});

function Root() {
  return (
    <>
      <ScrollRestoration />
      <Outlet />
    </>
  );
}

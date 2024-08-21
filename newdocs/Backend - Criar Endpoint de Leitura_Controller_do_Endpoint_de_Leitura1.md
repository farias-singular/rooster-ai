```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.GetBrandById
{
    [Route("api/organizations/{organizationId}/brands/{id}")]
    [ApiController]
    [ApiExplorerSettings(GroupName = "Brands")]
    public class GetBrandByIdController : Controller
    {
        /// <summary>
        /// Retrieves a Brand by its ID in the Organization tenant after an authorized client request.
        /// </summary>
        /// <param name="organizationId"></param>
        /// <param name="id"></param>
        /// <param name="mediator"></param>
        /// <returns></returns>
        [HttpGet]
        [Authorize]
        [ProducesResponseType(typeof(GetBrandByIdDto), StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        [ProducesResponseType(StatusCodes.Status401Unauthorized)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        [ProducesResponseType(StatusCodes.Status503ServiceUnavailable)]
        public async Task<IActionResult> GetBrandById(
            [FromRoute] string organizationId, 
            [FromRoute] string id,
            [FromServices] IMediator mediator)
        {
            var query = new GetBrandByIdQuery(
                id: id,
                organizationId: organizationId);

            var response = await mediator.Send(query);

            return Ok(response);
        }
    }
}
```
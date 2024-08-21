```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.CreateBrand
{
    [Route("api/organizations/{organizationId}/brands")]
    [ApiController]
    [ApiExplorerSettings(GroupName = "Brands")]
    public class CreateBrandController : Controller
    {
        /// <summary>
        /// Creates a new Brand in the Organization tenant after an authorized client request.
        /// </summary>
        /// <param name="organizationId"></param>
        /// <param name="request"></param>
        /// <param name="mediator"></param>
        /// <returns></returns>
        [HttpPost]
        [Authorize]
        [ProducesResponseType(typeof(CreateBrandDto), StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        [ProducesResponseType(StatusCodes.Status401Unauthorized)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        [ProducesResponseType(StatusCodes.Status503ServiceUnavailable)]
        public async Task<IActionResult> CreateBrand(
            [FromRoute] string organizationId, 
            [FromBody] CreateBrandRequest request, 
            [FromServices] IMediator mediator)
        {
            var command = new CreateBrandCommand(
                id: request.Id,
                organizationId: organizationId,
                categoryId: request.CategoryId,
                name: request.Name,
                title: request.Title);

            var response = await mediator.Send(command);

            return Ok(response);
        }
    }
}
```